## console outputs

* original:
      PARSER SETTINGS (see configuration_file(changed: configuration in targetid.py))
      _____________________
      DEV_EVAL_EPOCH_FREQUENCY:       3
      DROPOUT_RATE:   0.01
      EVAL_AFTER_EVERY_EPOCHS:        100
      HIDDEN_DIM:     100
      LEMMA_DIM:      100
      LSTM_DEPTH:     2
      LSTM_DIM:       100
      LSTM_INPUT_DIM: 100
      NUM_EPOCHS:     100
      PATIENCE:       25
      POS_DIM:        100
      PRETRAINED_EMBEDDING_DIM:       100

      TOKEN_DIM:      100
      TRAIN:  data/neural/fn1.7/fn1.7.fulltext.train.syntaxnet.conll
      UNK_PROB:       0.1
      USE_DROPOUT:    True

      # Tokens = 400572
              Unseen in dev/test = 45
              Unlearnt in dev/test = 390567
      # POS tags = 45
              Unseen in dev/test = 0
              Unlearnt in dev/test = 1
      # Lemmas = 9349
              Unseen in dev/test = 513
              Unlearnt in dev/test = 514

      _____________________

      type(esum(losses)): <class 'dynet_viz.Expression'>
      type((losses)): <class 'list'>
      type(trex_loss.npvalue()) <class 'NoneType'>
      type(trex_loss.scalar_value()) <class 'float'>
      trex_loss.scalar_value() 0.0

* after changing the return values in dynet_viz.py (obtained through pip install dynet, conda environment with python version 3.6 on windows, CPU version to avoid even more error)

      type(esum(losses)): <class 'dynet_viz.Expression'>
      type((losses)): <class 'list'>
      type(trex_loss.npvalue()) <class 'float'> <---
      type(trex_loss.scalar_value()) <class 'float'>
      trex_loss.scalar_value() 321.654 <---


      # changes in source code dynet_viz.py
      # def npvalue(self, recalculate=False): return None # the original code
      def npvalue(self, recalculate=False): return 123.456 # changed to test if loss=0 bug is triggered by this
