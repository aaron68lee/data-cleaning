#@begin SPOriginalOR2#@desc Workflow of Linear original openrefine history
#@param expression:grel:if(value < 0, 0, value)
#@param expression:grel:max(value, cells["price"].value)
#@param col-name:price
#@param expression:grel:if(isNull(value), 0, value)
#@param expression:value.toNumber()
#@param col-name:high_price
#@in table0
#@out table1
#@begin core/text-transform0#@desc Text transform on cells in column high_price using expression value.toNumber()
#@param col-name:high_price
#@param expression:value.toNumber()
#@in table0
#@out col:high_price1
#@end core/text-transform0
#@begin core/text-transform1#@desc Text transform on cells in column high_price using expression grel:if(isNull(value), 0, value)
#@param col-name:high_price
#@param expression:grel:if(isNull(value), 0, value)
#@in col:high_price1
#@out col:high_price2
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column high_price using expression grel:if(value < 0, 0, value)
#@param col-name:high_price
#@param expression:grel:if(value < 0, 0, value)
#@in col:high_price2
#@out col:high_price3
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column high_price using expression grel:max(value, cells["price"].value)
#@param col-name:high_price
#@param expression:grel:max(value, cells["price"].value)
#@in col:high_price3
#@out col:high_price4
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column price using expression value.toNumber()
#@param col-name:price
#@param expression:value.toNumber()
#@in table0
#@out col:price1
#@end core/text-transform4
#@begin core/text-transform5#@desc Text transform on cells in column price using expression grel:if(isNull(value), 0, value)
#@param col-name:price
#@param expression:grel:if(isNull(value), 0, value)
#@in col:price1
#@out col:price2
#@end core/text-transform5
#@begin core/text-transform6#@desc Text transform on cells in column price using expression grel:if(value < 0, 0, value)
#@param col-name:price
#@param expression:grel:if(value < 0, 0, value)
#@in col:price2
#@out col:price3
#@end core/text-transform6
#@begin MergeOperationsColumns #@desc Merge the Parallel Column operations
#@in col:high_price4
#@in col:price3
#@out table1
#@end MergeOperationsColumns
#@end SPOriginalOR2
