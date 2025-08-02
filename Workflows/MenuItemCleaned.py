#@begin LinearOriginalOR#@desc Workflow of Linear original openrefine history
#@param col-name:price
#@param expression:value.toNumber()
#@param col-name:high_price
#@param expression:grel:if(value < 0, 0, value)
#@param expression:grel:max(value, cells["price"].value)
#@param expression:grel:if(isNull(value), 0, value)
#@in table0
#@out table7
#@begin core/text-transform0#@desc Text transform on cells in column price using expression value.toNumber()
#@param col-name:price
#@param expression:value.toNumber()
#@in table0
#@out table1
#@end core/text-transform0
#@begin core/text-transform1#@desc Text transform on cells in column high_price using expression value.toNumber()
#@param col-name:high_price
#@param expression:value.toNumber()
#@in table1
#@out table2
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column high_price using expression grel:if(isNull(value), 0, value)
#@param col-name:high_price
#@param expression:grel:if(isNull(value), 0, value)
#@in table2
#@out table3
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column price using expression grel:if(isNull(value), 0, value)
#@param col-name:price
#@param expression:grel:if(isNull(value), 0, value)
#@in table3
#@out table4
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column price using expression grel:if(value < 0, 0, value)
#@param col-name:price
#@param expression:grel:if(value < 0, 0, value)
#@in table4
#@out table5
#@end core/text-transform4
#@begin core/text-transform5#@desc Text transform on cells in column high_price using expression grel:if(value < 0, 0, value)
#@param col-name:high_price
#@param expression:grel:if(value < 0, 0, value)
#@in table5
#@out table6
#@end core/text-transform5
#@begin core/text-transform6#@desc Text transform on cells in column high_price using expression grel:max(value, cells["price"].value)
#@param col-name:high_price
#@param expression:grel:max(value, cells["price"].value)
#@in table6
#@out table7
#@end core/text-transform6
#@end LinearOriginalOR
