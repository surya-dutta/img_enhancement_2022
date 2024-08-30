ref = imread("image.jpg");
A = imread("_UDCP.jpg")
[ssimval,ssimmap] = ssim(A,ref);
  
imshow(ssimmap,[])
title(['Local SSIM Map with Global SSIM Value: ',num2str(ssimval)])
