import wandb

run = wandb.init(
    project="debug-tests",
    entity="drewmacl-uchicago",
    settings=wandb.Settings(start_method="thread", _disable_stats=True)
)

print("Started run:", run.name)
wandb.log({"test_metric": 1})
run.finish()

wandb.finish()