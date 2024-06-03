echo
echo "Create data folders"

mkdir -p ./dataset
mkdir -p ./dataset/spider-en
mkdir -p ./dataset/spider-gr

cd ./dataset

echo
echo "Download Spider Dataset"

gdown https://drive.google.com/uc?id=1iRDVHLr4mX2wQKSgA9J8Pire73Jahh0m
gdown --id 1iRDVHLr4mX2wQKSgA9J8Pire73Jahh0m

unzip spider.zip
cd ..

echo
echo "Downdload SMALL version of ENG Spider"

gdown https://drive.google.com/uc?id=1EHs2q6lOD7W0NltjOWe0NNsM_HubdzJ8
gdown https://drive.google.com/uc?id=1huPVUOlwP3zasNzZmWjNc8QA1L1arzqK
gdown https://drive.google.com/uc?id=1V8TuijPPpR2sGWVlh5J1PA5YAxBDvD09

cp ./dataset/spider/tables.json dataset/spider-en/
mv dev.json ./dataset/spider-en/
mv train_others.json ./dataset/spider-en/
mv train_spider.json ./dataset/spider-en/
ln -s $(pwd)/dataset/spider/database ./dataset/spider-en/database

echo
echo "Downdload SMALL version of GR Spider"

gdown https://drive.google.com/uc?id=1WcxPVo2rYecCXk_2fuT5aY8BMMt8Cuky
gdown https://drive.google.com/uc?id=1B9s1sj8a3AUTRlH6magKsDkPVk6ODNAI
gdown https://drive.google.com/uc?id=1SwW40nBwqghOtHBlFRDtG391XKzFMmty
gdown https://drive.google.com/uc?id=1u8cJ2PH6mfiDKZJRpEMBdnJfpmAlLGtZ

mv dev.json ./dataset/spider-gr/
mv tables.json ./dataset/spider-gr/
mv train_others.json ./dataset/spider-gr/
mv train_spider.json ./dataset/spider-gr/
ln -s $(pwd)/dataset/spider/database ./dataset/spider-gr/database

echo
echo "Cleanup"
rm -rf ./dataset/__MACOSX/
rm ./dataset/spider.zip

echo
echo "Setup completed"