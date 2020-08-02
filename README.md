# indexingXMLHansards.
- This programme has been developed for the purpose of Indexing transcribed records of debates in the Parliament of the Republic of South Africa (Hansards) using shared-memory parallel threads.
- The transcribed Hansards data is contained in an XML file which conforms to the AkomoNtoso XML schema. This data contains several debates that were held on different days and on these debates there are various speakers which participate in them.
- A Bitmap based index is generated for assisting users to search for which speakers that participate in any 2 debates within the dataset. 
- MPI is used to generate an index using shared-memory parallel threads.
- 2 different schemes for generating the indexes were generated and compared.
- Furthermore memory and CPU usage based benchmarks and optimizations are carried out to ensure program efficiency.

## RUNNING CODE
- For running the code the **make** command can be used.
- This will run 2 different schemes for generating indexes. The first scheme uses 3 threads, but only has 2 threads involved index generation and the second uses 4 threads. These schemes have varying performances which can be found in the benchmarking folder.
- Additionally this will run the automated search scheme that allows users to query the generated bitmap indexes.

## SEARCHING:
- For searching it was assumed that the user will know the names of the 2 debates which they intend to search along with the headings of those 2 debates and will enter them in the format:
**debate name: debate heading** 
NB: There is a space between the : and the start of the debate name.
- An example for a search that can be performed is shown below for searching the **opening** debate and the **debates** debate. The **debates** debate contains only 1 speaker who is the **president** while the **opening** debate has almost all speakers in the debates, including the **president**. 
- The query can be structured in the format:

* opening: TUESDAY, 8 MAY 1979
* debates: ALLEGED OMISSION OF WORDS FROM OFFICIAL REPORT OF SENATE DEBATES (HANSARD)

- The expected result from this search is for only the president speaker to be returned since this speaker is the only one who participates in both debates.

## BENCHMARKING

- Benchmarking data is in the Benchmarking folder.
- Within the folder, there is benchmarking data which was discussed in thoroughly on the report.
- The timing data was obtained from the use of the timeit module.
- For the timing data, 1000 samples were taken and the average an average time was computed from those samples.
- Memory usage during programme execution was profiled using the mprof plot module.
- There is also data obtained from cProfiling (Memory usage and CPU usage profiling) inside a separate folder within the benchmarking folder.
