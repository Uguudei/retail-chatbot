# retail-chatbot
Rasa retail demo chatbot

## Installation
Create venv in project file
```shell
python3 -m venv ./venv
pip install rasa
pip install --use-deprecated=legacy-resolver rasa-x --extra-index-url https://pypi.rasa.com/simple --upgrade
```

## Start rasa-x
```shell
rasa x --rasa-x-port 5003 --port 5006
```

## Rasa training
```shell
rasa data split nlu --training-fraction=0.1
rasa train nlu --random-seed 0
```

## Rasa validate
```shell
rasa validate nlu
```

### Rasa test stories
Rasa finds all files with test_ in system test it. Therefore, location of test file needs to be specified

```shell
rasa test core --stories tests/test_stories.yml --out results
rasa test nlu --nlu train_test_split/test_data.yml
rasa test nlu --nlu data/nlu.yml --cross-validation
```

## Clean /tmp directory in linux
```shell
# List big files in linux directory
du -sc * .[^.]* | sort -n
# Clean files one day prior
find /tmp -ctime 1 -exec rm -rf {} +
```
