export KEYS_PATH=the_dir_path_of_your_prepared_keys
export SECURE_PASSWORD_PATH=the_dir_path_of_your_prepared_password
export LOCAL_IP=your_local_ip_of_the_sgx_server
sudo docker run -itd \
    -e REDIS_HOST=127.0.0.1 \
    --privileged \
    --net=host \
    --cpuset-cpus="0-4" \
    --oom-kill-disable \
    --device=/dev/sgx \
    -v /var/run/aesmd/aesm.socket:/var/run/aesmd/aesm.socket \
    -v $KEYS_PATH:/opt/keys \
    -v $PWD/conf:/opt/conf \
    -v $SECURE_PASSWORD_PATH:/opt/password \
    --name=trusted-cluster-serving-local \
    -e LOCAL_IP=$LOCAL_IP \
    -e CORE_NUM=4 \
    intelanalytics/bigdl-ppml-trusted-realtime-ml-scala-occlum:2.0.0 \
    bash -c "export PATH=/opt/occlum/build/bin:$PATH && cd /opt/ && ./start-all.sh && tail -f /dev/null"
