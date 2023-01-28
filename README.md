# PYAD

Simple **Py**thon unsupervised and semi-supervised **A**nomaly **D**etection framework that implements deep and shallow machine learning models published in various papers.

## Models implemented

| Model     | Paper |
| --------- | ----- |
| ALAD      | [Adversarially Learned Anomaly Detection](https://arxiv.org/abs/1812.02288) |
| DAGMM     | [Deep Autoencoding Gaussian Mixture Model
For Unsupervised Anomaly Detection](https://bzong.github.io/doc/iclr18-dagmm.pdf) |
| DeepSVDD  | [Deep One-Class Classification](https://proceedings.mlr.press/v80/ruff18a.html) |
| DROCC | [DROCC: Deep Robust One-Class Classification](https://arxiv.org/abs/2002.12718) |
| DSEBM     | [Deep Structured Energy Based Models for Anomaly Detection](https://arxiv.org/abs/1605.07717) |
| GOAD | [Classification-Based Anomaly Detection for General Data](https://arxiv.org/abs/2005.02359) |
| SOM-DAGMM | [Self-Organizing Map assisted Deep Autoencoding Gaussian Mixture Model for Intrusion Detection](https://arxiv.org/pdf/2008.12686.pdf) |
| MemAE | [Memorizing Normality to Detect Anomaly: Memory-augmented Deep Autoencoder for Unsupervised Anomaly Detection](https://arxiv.org/abs/1904.02639) |
| NeuTraLAD | [Neural Transformation Learning for Deep Anomaly Detection Beyond Images](https://arxiv.org/abs/2103.16440) |
| OC-SVM | [Support Vector Method for Novelty Detection](https://proceedings.neurips.cc/paper/1999/file/8725fb777f25776ffa9076e44fcfd776-Paper.pdf) |
| LOF | [LOF: identifying density-based local outliers](https://dl.acm.org/doi/10.1145/335191.335388) |

## Installation

Using conda:

```bash
conda env create -f environment.yaml
```

Using pip:

```bash
pip install -r requirements.txt
```

## Reproduce experiments

The experiments are defined in YAML configuration files under [config](./config). Simply upload your data in the [data](./data) folder and use the preprocessing scripts to clean them or simply change the variables in `_data.yaml` to use a different path. Configurations are split in three different files: data, trainer and the model.

```bash
python main.py --config=./config/<data_fname> --config=./config/<trainer_fname> --config=./config/<model_fname>
```

where `<data_fname>`, `<trainer_fname>`, and `<model_fname>` refer respectively to the data, trainer, and model configuration files.

Example training an AutoEncoder on Arrhythmia:

```bash
python main.py --config=./config/_data.yaml --config=./config/_trainer.yaml --config=./config/autoencoder.yaml
```

### Powershell utility script

We also provide a [utility powershell script](./scripts/train.ps1) to automate training of multiple models on the same dataset. To launch it, simply run the following commands

```powershell
cd scripts
conda activate <my-env>
./train.ps1 <absolute-path-to-config> <data-config-fname> <trainer-config-fname>
```

where `<my-env>`, `<absolute-path-to-config>`, `<data-config-fname>`, and `<trainer-config-fname>` refer respectively to name of your conda environment, the absolute path to the configuration folder, the name of the data configuration file, and the name of the training configuration file.

Example on Arrhythmia:

```powershell
cd scripts
conda activate pyad
./train.ps1 C:\Users\me\path\to\pyad\config\arrhythmia _data.yaml _trainer.yaml
```

### Neptune logger

Optionally, you can log your experiments using Neptune. To do so, add a `logger` key in the `init_args` of the trainer and define `NEPTUNE_API_TOKEN` and `NEPTUNE_PROJECT` as environment variables.

```yaml
# _trainer.yaml
trainer:
  class_path: pyad.models.trainer.ModuleTrainer
  init_args:
    ...params
    logger:
      class_path: pyad.loggers.NeptuneLogger
```
