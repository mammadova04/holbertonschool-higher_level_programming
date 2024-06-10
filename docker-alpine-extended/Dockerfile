# Use the official Alpine base image
FROM alpine

# Install curl package
RUN apk add --no-cache curl

# Copy config.txt to the container
COPY config.txt /app/config.txt

# Set the command to print "Hello, World!" (same as previous)
CMD ["echo", "Hello, World!"]
