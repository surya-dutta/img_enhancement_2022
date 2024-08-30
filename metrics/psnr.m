ref = imread("image.jpg");
A = imread("DCP.jpg")
[peaksnr, snr] = psnr(A, ref);
  
fprintf('\n The Peak-SNR value is %0.4f', peaksnr);
