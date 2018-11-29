      python3 -m sesame.preprocess

      python3 -m sesame.targetid --mode train --model_name fn1.7-targetid
      python3 -m sesame.frameid --mode train --model_name fn1.7-frameid
      python3 -m sesame.argid --mode train --model_name fn1.7-argid

      python3 -m sesame.targetid --mode test --model_name fn1.7-targetid
      python3 -m sesame.frameid --mode test --model_name fn1.7-frameid
      python3 -m sesame.argid --mode test --model_name fn1.7-argid

      python3 -m sesame.targetid --mode predict --model_name fn1.7-targetid --raw_input data/sentences.txt
      python3 -m sesame.frameid --mode predict --model_name fn1.7-frameid --raw_input logs/fn1.7-targetid/predicted-targets.conll
      python3 -m sesame.argid --mode predict --model_name fn1.7-argid --raw_input logs/fn1.7-frameid/predicted-frames.conll

   -------------------


      python -m sesame.preprocess

      python -m sesame.targetid --mode train --model_name fn1.7-targetid
      python -m sesame.frameid --mode train --model_name fn1.7-frameid
      python -m sesame.argid --mode train --model_name fn1.7-argid

      python -m sesame.targetid --mode test --model_name fn1.7-targetid
      python -m sesame.frameid --mode test --model_name fn1.7-frameid
      python -m sesame.argid --mode test --model_name fn1.7-argid

      python -m sesame.targetid --mode predict --model_name fn1.7-targetid --raw_input data/sentences.txt
      python -m sesame.frameid --mode predict --model_name fn1.7-frameid --raw_input logs/fn1.7-targetid/predicted-targets.conll
      python -m sesame.argid --mode predict --model_name fn1.7-argid --raw_input logs/fn1.7-frameid/predicted-frames.conll
