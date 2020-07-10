

# RUNNING CODE
For running the code the **make** command can be used

# SEARCHING:
- For searching it was assumed that the user will know the names of the 2 debates which they intend to search along with the headings of those 2 debates and will enter them in the format:
**debate name: debate heading** 
NB: There is a space between the : and the start of the debate name.
- An example for a search that can be performed is shown below for searching the **opening** debate and the **debates** debate. The **debates** debate contains only 1 speaker who is the **president** while the **opening** debate has almost all speakers in the debates, including the **president**. 
- The query can be structured in the format:

* opening: TUESDAY, 8 MAY 1979
* debates: ALLEGED OMISSION OF WORDS FROM OFFICIAL REPORT OF SENATE DEBATES (HANSARD)

- The expected result from this search is for only the president speaker to be returned since this speaker is the only one who participates in both debates.

# BENCHMARKING

- Benchmarking data is in the Benchmarking folder.
- Within the folder, there is benchmarking data which was discussed in thoroughly on the report.
- The timing data was obtained from the use of the timeit module.
- For the timing data, 1000 samples were taken and the average an average time was computed from those samples.
- Memory usage during programme execution was profiled using the mprof plot module.
- There is also data obtained from cProfiling (Memory usage and CPU usage profiling) inside a separate folder within the benchmarking folder.
