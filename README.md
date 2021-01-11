Read more on Medium: https://imgraham1996.medium.com/building-deploying-a-vertical-search-engine-from-scratch-a48bde9447aa
Test it out: http://imgraham1.pythonanywhere.com/

Here, I build a vertical search engine from scratch by collecting data, implementing ranking functions, and deploying it.<br><br>
I begin by scraping over 1,800 articles related to space flight from sources like NASA and Wikipedia. Once I had all of the documents I processed and cleaned them by dropping short documents, truncating long documents, removing stop-words, and converting to lowercase. <br><br>
I implemented a baseline of returning documents with the highest term-frequency counts to guage how well other methods perform. I used multiple term weighting approaches for ranking (more details can be found in the Medium write up) and used precision and recall as the metrics for evaluation.
