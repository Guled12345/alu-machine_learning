def load_model(self):
    """
    Creates the model used to calculate cost from VGG19 Keras base model

    Model's input should match VGG19 input
    Model's output should be a list containing outputs of VGG19 layers
        listed in style_layers followed by content_layers

    Saves the model in the instance attribute model
    """
    VGG19_model = tf.keras.applications.VGG19(include_top=False,
                                              weights='imagenet')
    VGG19_model.save("VGG19_base_model")
    custom_objects = {'MaxPooling2D': tf.keras.layers.AveragePooling2D}

    vgg = tf.keras.models.load_model("VGG19_base_model",
                                     custom_objects=custom_objects)

    style_outputs = []
    content_output = None

    for layer in vgg.layers:
        if layer.name in self.style_layers:
            style_outputs.append(layer.output)
        if layer.name == self.content_layer:
            content_output = layer.output

        layer.trainable = False

    outputs = style_outputs + [content_output]

    model = tf.keras.models.Model(vgg.input, outputs)
    self.model = model
