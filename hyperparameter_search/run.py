import hpsearch

hpsearch.hpsearch(
    "fine_tune_bert_dm_nina",
    "days.w2d4.fine_tune_bert.train",
    "days/w2d4/fine_tune_bert.gin",
    {"train.lr": [1e-4, 1e-5], "set_random_seed.seed": [0,1,2]},
    comet_key="",
    local=False,
)