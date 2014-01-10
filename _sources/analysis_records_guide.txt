.. _doc-analysis-records-guide:


************************
Analysis Records
************************

.. figure:: _static/protocol-analysisrecord.png
    :align: right

``AnalysisRecords`` describe a single step of analysis in the chain from *Measurements* to “final” result (yeah, we know—science is never really done!). An ``AnalysisRecord`` associates inputs—*Measurements* or the outputs of other *AnalysisRecords*, a *Protocol*, ``analysisParameters`` (like ``protocolParameters`` for a *Procedure*) and the results (“outputs”).


.. figure:: _static/chained-analysis-records.png
    :align: center
    
    **AnalysisRecords can be chained**

*AnalysisRecords* can be chained using the output of one *AnalysisRecord* as the input to “downstream” *AnalysisRecords*. Use chained records to keep track of how you got from your (awesome) *Measurements* to your (awesome) results! And just in case you realize that you need to redo part of an analysis (we’ve been there!), you can use these *AnalysisRecord* chains to find all of the downstream analyses that should also be revisited.