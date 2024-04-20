# Use the official Python image from the Docker Hub
FROM python

# Set the working directory in the container
WORKDIR /app

# Copy the Python script and the text file into the container
COPY paragraphs.py /app
COPY paragraphs.txt /app

# Install NLTK and its data
RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

# Run the Python script when the container launches
CMD ["python", "paragraphs.py"]
