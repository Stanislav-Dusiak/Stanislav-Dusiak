import torch
from abc import ABC, abstractmethod


def calc_out_shape(input_matrix_shape, out_channels, kernel_size, stride,
                   padding):
    batch_size, channels_count, input_height, input_width = input_matrix_shape
    output_height = (input_height + 2 * padding - (
            kernel_size - 1) - 1) // stride + 1
    output_width = (input_width + 2 * padding - (
            kernel_size - 1) - 1) // stride + 1

    return batch_size, out_channels, output_height, output_width


class ABCConv2d(ABC):
    def __init__(self, in_channels, out_channels, kernel_size, stride):
        self.in_channels = in_channels
        self.out_channels = out_channels
        self.kernel_size = kernel_size
        self.stride = stride

    def set_kernel(self, kernel):
        self.kernel = kernel

    @abstractmethod
    def __call__(self, input_tensor):
        pass


class Conv2d(ABCConv2d):
    def __init__(self, in_channels, out_channels, kernel_size, stride):
        self.conv2d = torch.nn.Conv2d(in_channels, out_channels, kernel_size,
                                      stride, padding=0, bias=False)

    def set_kernel(self, kernel):
        self.conv2d.weight.data = kernel

    def __call__(self, input_tensor):
        return self.conv2d(input_tensor)


def create_and_call_conv2d_layer(conv2d_layer_class, stride, kernel,
                                 input_matrix):
    out_channels = kernel.shape[0]
    in_channels = kernel.shape[1]
    kernel_size = kernel.shape[2]

    layer = conv2d_layer_class(in_channels, out_channels, kernel_size, stride)
    layer.set_kernel(kernel)

    return layer(input_matrix)


def test_conv2d_layer(conv2d_layer_class, batch_size=2,
                      input_height=4, input_width=4, stride=2):
    kernel = torch.tensor(
        [[[[0., 1, 0],
           [1, 2, 1],
           [0, 1, 0]],

          [[1, 2, 1],
           [0, 3, 3],
           [0, 1, 10]],

          [[10, 11, 12],
           [13, 14, 15],
           [16, 17, 18]]]])

    in_channels = kernel.shape[1]

    input_tensor = torch.arange(0, batch_size * in_channels *
                                input_height * input_width,
                                out=torch.FloatTensor()) \
        .reshape(batch_size, in_channels, input_height, input_width)

    custom_conv2d_out = create_and_call_conv2d_layer(
        conv2d_layer_class, stride, kernel, input_tensor)
    conv2d_out = create_and_call_conv2d_layer(
        Conv2d, stride, kernel, input_tensor)

    return torch.allclose(custom_conv2d_out, conv2d_out) \
           and (custom_conv2d_out.shape == conv2d_out.shape)


# Convolutional layer through cycles.
class Conv2dLoop(ABCConv2d):
    def __call__(self, input_tensor):
        padding = 0  # Under the terms of the task padding = 0
        output_tensor_shape = calc_out_shape(input_tensor.shape,
                                             # Determine the dimension of the output tensor
                                             self.out_channels,
                                             self.kernel_size,
                                             self.stride,
                                             padding)

        output_tensor = torch.zeros(
            output_tensor_shape)  # Creating a template for the output tensor

        in_img_num = input_tensor.shape[0]  # Number of input images
        in_img_channel_num = input_tensor.shape[
            1]  # Number of channels in each input image
        filter_num = output_tensor_shape[1]  # Number of filters
        filter_height = self.kernel_size  # Height of filter
        filter_width = self.kernel_size  # Width of filter
        out_img_height = output_tensor_shape[2]  # Height of the output image
        out_img_width = output_tensor_shape[3]  # Width of the output image

        for f in range(filter_num):  # For each filter
            for i in range(in_img_num):  # For each image
                for c in range(in_img_channel_num):  # For each channel in the filter and image
                    for m in range(0, out_img_height):  # For each row of the output image
                        for n in range(0, out_img_width):  # For each column of the output image
                            # Counting the element-by-element multiplication of tensors
                            temp = self.kernel[f, c] * input_tensor[i, c,
                                                       m * self.stride: m * self.stride + filter_height,
                                                       n * self.stride: n * self.stride + filter_width]
                            # Sum up the multiplication results and combine the filters
                            output_tensor[i, f, m, n] += temp.sum()
        return output_tensor


print(test_conv2d_layer(Conv2dLoop))

