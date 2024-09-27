% Use this editor as a MiniZinc scratch book
include "alldifferent.mzn";

var 1..9: d1;  
var 0..9: d2; 
var 0..9: d3; 
var 0..9: d4; 
var 0..9: d5;  
var 0..9: d6; 

constraint alldifferent([d1, d2, d3, d4, d5, d6]);

constraint d1 + d2 + d3 = d4 + d5 + d6;

solve minimize d1 + d2 + d3; 