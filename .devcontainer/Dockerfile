########### Image file ###########
FROM python:3-buster
##################################

########### update and install packages ###########
# apt-get upgradeに-yを付けないとexit 1になります．追加しました．(5/23)
RUN apt-get update && \
    apt-get -y upgrade && \
    apt-get install -y vim git graphviz graphviz-dev && \
    rm -rf /var/lib/apt/lists*
###################################################

########## add user ########## 
ARG USERNAME=user
ARG GROUPNAME=user 
ARG UID=1000
ARG GID=1000
RUN groupadd -g ${GID} ${GROUPNAME} && \
    useradd -m -s /bin/bash -u ${UID} -g ${GID} ${USERNAME}
USER ${USERNAME}
##############################

########### create workspace ###########
RUN mkdir /home/${USERNAME}/code 
WORKDIR /home/${USERNAME}/code
ADD ./requirements.txt /home/${USERNAME}/code
########################################

########### install packages via pip ###########
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
ADD . /home/${USERNAME}/code/
################################################
