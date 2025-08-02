
#@begin LinearOriginalOR#@desc Workflow of Linear original openrefine history
#@param col-name:event
#@param expression:value.toString()
#@param expression:value.toUppercase()
#@param expression:grel:if(isNull(value), "X", value)
#@param expression:value.replace(/[\p{Zs}\s]+/,' ')
#@param expression:value.trim()
#@in table0
#@out table6
#@begin core/mass-edit0#@desc Mass edit cells in column event
#@param col-name:event
#@in table0
#@out table1
#@end core/mass-edit0
#@begin core/text-transform0#@desc Text transform on cells in column event using expression value.trim()
#@param col-name:event
#@param expression:value.trim()
#@in table1
#@out table2
#@end core/text-transform0
#@begin core/text-transform1#@desc Text transform on cells in column event using expression value.toUppercase()
#@param col-name:event
#@param expression:value.toUppercase()
#@in table2
#@out table3
#@end core/text-transform1
#@begin core/text-transform2#@desc Text transform on cells in column event using expression value.replace(/[\p{Zs}\s]+/,' ')
#@param col-name:event
#@param expression:value.replace(/[\p{Zs}\s]+/,' ')
#@in table3
#@out table4
#@end core/text-transform2
#@begin core/text-transform3#@desc Text transform on cells in column event using expression value.toString()
#@param col-name:event
#@param expression:value.toString()
#@in table4
#@out table5
#@end core/text-transform3
#@begin core/text-transform4#@desc Text transform on cells in column event using expression grel:if(isNull(value), "X", value)
#@param col-name:event
#@param expression:grel:if(isNull(value), "X", value)
#@in table5
#@out table6
#@end core/text-transform4
#@end LinearOriginalOR
