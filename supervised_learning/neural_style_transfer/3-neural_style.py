#!/usr/bin/env python3
"""
Defines class NST that performs tasks for neural style transfer
"""

import numpy as np
import tensorflow as tf

class NST:
    """
    Performs tasks for Neural Style Transfer
    """
    style_layers = ['block1_conv1', 'block2_conv1', 'block3_conv1',
                    'block4_conv1', 'block5_conv1']
    content_layer = 'block5_conv2'

    def __init__(self, style_image, content_image, alpha=1e4, beta=1):
        if not isinstance(style_image, np.ndarray) or style_image.shape[-1] != 3:
            raise TypeError("style_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(content_image, np.ndarray) or content_image.shape[-1] != 3:
            raise TypeError("content_image must be a numpy.ndarray with shape (h, w, 3)")
        if not isinstance(alpha, (float, int)) or alpha < 0:
            raise TypeError("alpha must be a non-negative number")
        if not isinstance(beta, (float, int)) or beta < 0:
            raise TypeError("beta must be a non-negative number")

        self.style_image = self.scale_image(style_image)
        self.content_image = self.scale_image(content_image)
        self.alpha = alpha
        self.beta = beta
        self.model = self.load_model()
        self.generate_features()

    @staticmethod
    def scale_image(image):
        if not isinstance(image, np.ndarray) or image.shape[-1] != 3:
            raise TypeError("image must be a numpy.ndarray with shape (h, w, 3)")

        h, w, _ = image.shape
        if h > w:
            new_h, new_w = 512, int(512 * w / h)
        else:
            new_w, new_h = 512, int(512 * h / w)

        image = tf.image.resize(image, (new_h, new_w), method='bicubic')
        image = image / 255.0
        image = tf.clip_by_value(image, 0.0, 1.0)
        return tf.expand_dims(image, axis=0)

    def load_model(self):
        vgg = tf.keras.applications.VGG19(include_top=False, weights='imagenet')
        vgg.trainable = False

        outputs = [vgg.get_layer(name).output for name in self.style_layers + [self.content_layer]]
        model = tf.keras.models.Model([vgg.input], outputs)
        return model

    @staticmethod
    def gram_matrix(input_layer):
        if not isinstance(input_layer, (tf.Tensor, tf.Variable)):
            raise TypeError("input_layer must be a tensor")

        result = tf.linalg.einsum('bijc,bijd->bcd', input_layer, input_layer)
        num_locations = tf.cast(tf.reduce_prod(input_layer.shape[1:3]), tf.float32)
        return result / num_locations

    def generate_features(self):
        preprocessed_style = tf.keras.applications.vgg19.preprocess_input(self.style_image * 255)
        preprocessed_content = tf.keras.applications.vgg19.preprocess_input(self.content_image * 255)

        style_outputs = self.model(preprocessed_style)
        content_outputs = self.model(preprocessed_content)

        self.gram_style_features = [self.gram_matrix(style_output) for style_output in style_outputs[:-1]]
        self.content_feature = content_outputs[-1]
