FROM ubuntu:18.04

# Install stuff
RUN apt-get update && \
    apt-get install -y zip && \
    apt-get install -y openssh-server && \ 
    apt-get install sudo -y && \
    apt-get install xxd -y && \
    apt-get install vim -y

# Setup Challenge
COPY files/setup.sh .
RUN ./setup.sh
RUN rm ./setup.sh
COPY files/file.txt /home/ritsec/file.txt
COPY files/intro.py /bin/intro.py
COPY files/.bash_profile /home/ritsec/.bash_profile
COPY files/.bashrc /home/ritsec/.bashrc
COPY files/.supersecret.txt /usr/hackerman1337/.supersecret.txt
COPY files/.bash_history /home/ritsec/.bash_history
COPY files/1 /tmp/1
COPY files/hard.txt /home/hard/hard.txt

# Setup SSH
RUN mkdir /var/run/sshd
RUN sed -i 's/PermitRootLogin prohibit-password/PermitRootLogin no/' /etc/ssh/sshd_config

# SSH login fix. Otherwise user is kicked off after login
RUN sed 's@session\s*required\s*pam_loginuid.so@session optional pam_loginuid.so@g' -i /etc/pam.d/sshd

ENV NOTVISIBLE "in users profile"
RUN echo "export VISIBLE=now" >> /etc/profile

EXPOSE 22
CMD ["/usr/sbin/sshd", "-D"]