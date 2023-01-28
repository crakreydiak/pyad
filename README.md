# PYAD

Simple Python unsupervised and semi-supervised Anomaly Detection framework that implements deep and shallow machine learning models published in various papers.

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

| SOM-DAGMM | [Self-Organizing Map assisted Deep Autoencoding
Gaussian Mixture Model for Intrusion Detection](https://arxiv.org/pdf/2008.12686.pdf) |
| MemAE | [Memorizing Normality to Detect Anomaly: Memory-augmented Deep Autoencoder for Unsupervised Anomaly Detection](https://arxiv.org/abs/1904.02639) |
| NeuTralAD | [Neural Transformation Learning for Deep Anomaly Detection Beyond Images](https://arxiv.org/abs/2103.16440) |
| OC-SVM | [Support Vector Method for Novelty Detection](https://proceedings.neurips.cc/paper/1999/file/8725fb777f25776ffa9076e44fcfd776-Paper.pdf) |
| LOF | [LOF: identifying density-based local outliers](https://dl.acm.org/doi/10.1145/335191.335388) |

## Installation

```bash
conda env create -f environment.yaml
```

## Reproduce experiments

To easily reproduce the experiments of our paper, the papers are set in configuration files. Simply load your data in the [data](./data) folder and use the preprocessing scripts to clean them. To set a different location, simply change the variables in `_data.yaml`.
