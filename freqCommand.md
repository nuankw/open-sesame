      python -m sesame.targetid --mode train --model_name fn1.7-targetid

      python -m sesame.targetid --mode predict --model_name fn1.7-targetid --raw_input data/sentences.txt
      python -m sesame.frameid --mode predict --model_name fn1.7-frameid --raw_input logs/fn1.7-pretrained-targetid/predicted-targets.conll
      python -m sesame.argid --mode predict --model_name fn1.7-argid --raw_input logs/fn1.7-pretrained-frameid/predicted-frames.conll
