BERT_LARGE_DIR=$HOME'/bert/BERT_Large_uncased_L-24_H-1024_A-16'
BERT_BASE_DIR=$HOME'/bert/BERT_Base_uncased_L-12_H-768_A-12'
BERT_MODEL_DIR=$BERT_BASE_DIR
python run_squad.py \
  --vocab_file=$BERT_MODEL_DIR/vocab.txt \
  --bert_config_file=$BERT_MODEL_DIR/bert_config.json \
  --init_checkpoint=$BERT_MODEL_DIR/bert_model.ckpt \
  --do_predict=True \
  --predict_file=$SQUAD_DIR/project_data/dev-v2.0.json \
  --train_batch_size=6 \
  --learning_rate=3e-5 \
  --num_train_epochs=2.0 \
  --max_seq_length=384 \
  --doc_stride=128 \
  --output_dir=outputs/squad/ \
  --use_tpu=False\
  --version_2_with_negative=True
