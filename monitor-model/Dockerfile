FROM python:3.13-alpine

# Install git
RUN apk add --no-cache git

# Create app directory
WORKDIR /app

# Install app dependencies
COPY ./requirements.txt ./
RUN pip install -r requirements.txt

# Bundle app source
COPY ./ /app

WORKDIR /app/source
ENTRYPOINT [ "python", "main.py" ]

# CMD [ "./run_monitor.sh" ] 

# RUN echo "0 4 */2 * * python /app/source/main.py >> /app/logs/cron.log 2>&1" > /app/monitor_cron

# # Apply the cron job
# RUN crontab /app/monitor_cron

# # Run the command on container startup
# CMD crond && tail -f /app/logs/cron.log