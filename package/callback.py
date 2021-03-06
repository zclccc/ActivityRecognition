# Author : DINDIN Meryll
# Date : 17/06/2017

from package.imports import *

# Defines the callback for merge on the adaptive dropout

class DecreaseDropout(Callback):

    # Initialization
    def __init__(self, prb, steps):

        super(Callback, self).__init__()

        self.ini = prb
        self.prb = prb
        self.steps = steps

    # Changes the dropout rate depending on the epoch
    def on_epoch_end(self, epoch, logs=None):

        self.prb = max(0, 1 - epoch/self.steps) * self.ini

# Layer corresponding to the adaptive dropout

class AdaptiveDropout(Layer):

    # Initialization
    def __init__(self, p, callback, **kwargs):

        self.p = p
        self.callback = callback
        if 0. < self.p < 1.: self.uses_learning_phase = True
        self.supports_masking = True

        super(AdaptiveDropout, self).__init__(**kwargs)

    # Defines the core operation of the layer
    def call(self, x, mask=None):

        self.p = self.callback.prb

        if 0. < self.p < 1.:
            x = K.in_train_phase(K.dropout(x, level=self.p), x)

        return x

    # Returns config for serialization
    def get_config(self):

        config = {'p': self.p}
        base_config = super(AdaptiveDropout, self).get_config()

        return dict(list(base_config.items()) + list(config.items()))

# Aims at shuffling the data for better generalization

class DataShuffler(Callback):

    # Initialization
    # dtb_path refers to the database path
    # rounds refers to the amount of rounds for which the data is shuffled
    def __init__(self, dtb_path, rounds):

        super(Callback, self).__init__()

        self.pth = dtb_path
        self.rnd = rounds

    # Shuffles the data at each end of epoch
    def on_epoch_end(self, epoch, logs=None):

        if epoch % self.rnd == 0:

            with h5py.File(self.pth, 'a') as dtb:

                i_t = shuffle(np.arange(dtb['label_t'].shape[0]))
                for key in [ele for ele in dtb.keys() if ele[-1] == 't']:
                    dtb[key][...] = dtb[key].value[i_t]

        else: pass

        return
