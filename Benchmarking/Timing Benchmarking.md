
# BenchmakingOddandEven

<table>
<thead>
<tr>
  <th>Tasks Performed</th>
  <th>Time In seconds</th>
</tr>
</thead>
<tbody>
<tr>
<td>index calculation even odd in rank  2 </td>  
<td>0.012296201064000116s </td>
</tr>
<tr>
<td>index calculation even odd in rank  1 </td>  
<td>0.015022688058000085s </td>
</tr>
<tr>
<td>Sending back to row 0 from even odd in rank  1 </td> 
<td>0.00012408166900013383s </td>
</tr>
<tr>
<td>Sending back to row 0 from even odd in rank  2 </td>  <td>0.00013604402600003596s </td>
</tr>
<tr>
<td>Initial sending from even odd rank  0   </td>
<td>0.5419628143310546s </td>
</tr>
<tr>
<td>Recieving in rank  1  from rank 1  </td>
<td>0.6087393760681152s </td>
</tr>
<tr>
<td>Recieving in rank  2  from rank 1  </td>
 <td>0.8635344505310059s </td>
</tr>
<tr>
<td>Recieving in rank  0  from rank 1 and 2 </td>
 <td>0.17752528190612793s </td>
</tr>
<tr>
<td>Final index construction even odd in rank  0   </td>
<td>0.00037298683100016203s </td>
</tr>
<tr>
<td>Debate dicitonary creation even odd in rank  0   </td>
 <td>0.0020051576629998634s </td>
 </tr>
<tr>
<td>Speaker dicitonary creation even odd in rank  0   </td>
 <td>0.011024270315999729s </td>
</tr>
</tbody>
</table>

# Benchmarking4threads

<table>
<thead>
<tr>
  <th>Tasks Performed</th>
  <th>Time In seconds</th>
</tr>
</thead>
<tbody>
<tr>
<td>debate dictionary creation in rank  0</td> 
<td>0.0034693366639999114s</td>
</tr>
<tr>
<td>speaker dictionary creation in rank  0</td> 
<td> 0.017169719506999626s</td>
</tr>
<tr>
<td>index calculation even odd in rank  0 </td>
<td> 0.0031448472029000185s</td>
</tr>
<tr>
<td>index calculation even odd in rank  3</td> 
<td> 0.0034088584969999827s</td>
</tr>
<tr>
<td>index calculation even odd in rank  2</td> 
<td>0.005942345047999879s</td>
</tr>
<tr>
<td>index calculation even odd in rank  1</td>
<td>0.006805153051000161s</td>
</tr>
<tr>
<td>final bitmap construction 4 threads in rank  0</td>
<td>1.878090800028076e-05s</td>
</tr>
<tr>
<td>receiving in rank  0 </td>
<td>0.08362507820129395s</td>
</tr>
<tr>
<td>receiving in rank  1  </td>
<td>0.2611372470855713s</td>
</tr>
<tr>
<td>receiving in rank  2  </td>
<td>0.35106849670410156s</td>
</tr>
<tr>
<td>receiving in rank  3  </td>
<td>0.4577140808105469s</td>
</tr>
<tr>
<td>sending in rank  0  </td>
<td>0.2069721221923828s</td>
</tr>
<tr>
<td>sending in rank  1  </td>
<td>0.00021600723266601562s</td>
</tr>
<tr>
<td>sending in rank  2  </td>
<td>0.00017786026000976562s</td>
</tr>
<tr>
<td>sending in rank  3  </td>
<td>0.0001761913299560547s</td>
</tr>
</tbody>
</table>

