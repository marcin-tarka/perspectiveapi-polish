# PerspectiveAPI-polish

Code for experiment which duplitates [1] on text translated from English to Polish by translate.google.com

## About

The aim of the experiment was to duplicate experiment described in [1], using the same text but automatically translated using google translator. The simplest of descibed in [1] algorithms was used, namely logistic regression [2].

## The code

Repository cointains scripts used for automatic translation and Jupyter notebooks with results:
* attack_translator_divider.py - script which divides original data into subfiles. Subfiles were used as a workaround for google API daily requests limit.
* attack_translator.py - script which makes a translation.
* attact_translator_composer.py - script which composes partial files into one result. Stored in data/attack_pl.csv.
* perspective_attack.ipynb - logistic regression on English data.
* perspective_attack_pl.ipynb - logistic regression on Polish data.
* data/attack_pl.csv - data for Polish experiment.
* data/attack_annotations.tsv - data annotations.

## Results

ROC AUC metric was used to examine both Polish and English classifier. Result for Polish was 0.916, while for English 0.958.

## Bibliography
[1] Ellery Wulczyn, Nithum Thain, Lucas Dixon "Ex Machina: Personal Attacks Seen at Scale" https://arxiv.org/abs/1610.08914
[2] http://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
[3] https://www.perspectiveapi.com