sudo apt-get --assume-yes install build-essential autoconf automake libpcre3-dev libevent-dev pkg-config zlib1g-dev libssl-dev
sudo apt-get --assume-yes install git
sudo git clone https://github.com/RedisLabs/memtier_benchmark.git
cd memtier_benchmark
sudo autoreconf -ivf
sudo ./configure --disable-tls
sudo make
sudo make install