function gaussianPDF(mean, variance, x){
  standardDeviation = Math.sqrt(variance);
  var m = standardDeviation * Math.sqrt(2 * Math.PI);
  var e = Math.exp(-Math.pow(x - mean, 2) / (2 * variance));
  return e / m;
}