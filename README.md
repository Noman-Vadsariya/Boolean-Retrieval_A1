# Boolean-Retrieval_A1

Description

    Boolean Retrieval Model have been implemented, which can process Boolean user query that can only be formed by joining three (or more) terms (t1, t2 and t3) with (AND, OR and NOT) Boolean operators. It can also process For positional queries, the query text contains “/” along with a k intended to return all documents that contains t1 and t2, k words apart on either side of the text

Inverted Index Structure

    Dictionary - key = Vocablary term  :  Value = list of docId in which term appears

    { "term1" : [docIDs] , "term2" : [docIds] , "term2" : [docIds], ..... , , "termN" : [docIds]}

Positional Index Structure

    {Vocablary term : {"docId in which term appears" : [postions at which term appear in that document] } }

    { "term1" : { "docId1" : [postions] , "docId2" : [postions] } , "term2" : { "docId1" : [postions] , "docId2" : [postions] },
     .... "termN" : { "docId1" : [postions] , "docId2" : [postions] } }

Dependencies

    pip install flask

Run

    python app.py
