# wget http://download.redis.io/releases/redis-5.0.5.tar.gz
tar xzf redis-5.0.5.tar.gz
sudo mv redis-5.0.5 /etc/redis
cd /etc/redis
sudo apt-get install make
sudo apt-get install gcc
sudo aptitude install build-essential

# cd deps
# sudo make hiredis jemalloc linenoise lua geohash-int
# cd ..

sudo make
sudo apt-get install tcl8.5
# make test (optional)
sudo make install
cd utils
sudo REDIS_PORT=6378 REDIS_CONFIG_FILE=/etc/redis/6378.conf REDIS_LOG_FILE=/var/log/redis_6378.log  REDIS_DATA_DIR=/var/lib/redis/6378 REDIS_EXECUTABLE=`command -v redis-server` /etc/redis/utils/install_server.sh
