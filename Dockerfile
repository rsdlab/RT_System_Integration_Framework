# osrfが提供するrosイメージ（タグがnoetic-desktop-full）をベースとしてダウンロード
FROM osrf/ros:noetic-desktop-full
# Docker実行してシェルに入ったときの初期ディレクトリ（ワークディレクトリ）の設定

RUN apt update && apt install -y curl python3 python3-pip git python-is-python3 wget emacs 


ARG USERNAME=rsdlab
ARG GROUPNAME=rsdlab
ARG UID=1000
ARG GID=1000
ARG PASSWORD=rsdlab
RUN groupadd -g $GID $GROUPNAME && \
    useradd -m -s /bin/bash -u $UID -g $GID -G sudo $USERNAME && \
    echo $USERNAME:$PASSWORD | chpasswd && \
    echo "$USERNAME   ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
USER $USERNAME
WORKDIR /home/$USERNAME/

RUN echo "source /opt/ros/noetic/setup.sh" >> .bashrc

RUN mkdir -p catkin_ws/src && cd catkin_ws/src \
    && . /opt/ros/noetic/setup.sh \
    && catkin_init_workspace \
    && cd && cd catkin_ws \
    && . /opt/ros/noetic/setup.sh \ 
    && catkin_make \
    && echo "source ./catkin_ws/devel/setup.bash" >> .bashrc

RUN ["/bin/bash", "-c", "bash <(curl -s https://raw.githubusercontent.com/OpenRTM/OpenRTM-aist/master/scripts/openrtm2_install_ubuntu.sh) -l all --yes -e ros"]

ENV USER $USERNAME

RUN mkdir workspace && cd workspace && git clone https://github.com/rsdlab/wasanbon && cd wasanbon && sudo python setup.py install && wasanbon-admin.py environment init -v && wasanbon-admin.py environment setup_bashrc && wasanbon-admin.py binder update -v
RUN pip install pyqtspinner

COPY  system system/ 
COPY  sample2 catkin_ws/src/.

