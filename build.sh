cd builder
bash setup.sh
pip install -r requirements.txt
python cache_models.py
cd ../src
python rp_handler.py --rp_serve_api --rp_api_host='0.0.0.0'
python request_it.py
