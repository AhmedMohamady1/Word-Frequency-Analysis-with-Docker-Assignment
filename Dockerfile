# Use python alpine from the docker repository
FROM python:alpine

# Set the directory in the container
WORKDIR /app

# Copy the Python script and the text file into the container
COPY paragraphs.py /app
COPY paragraphs.txt /app

# Install NLTK its packages (stopwords and punkt for word_tokenize)
RUN pip install nltk
RUN python -m nltk.downloader stopwords
RUN python -m nltk.downloader punkt

# Run the Python script when the container launches
CMD ["python", "paragraphs.py"]
