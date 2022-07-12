# A.I._Enabled_Vaccination_Verification
Utilizing cutting edge Artificial Intelligence to create a robust, effective and automated vaccination verification process

![MainWindow](https://user-images.githubusercontent.com/72056829/178451224-d563d1e5-ddf9-4829-a3ba-30ba42315039.png)

## Requirements: 

    - Python 64 bit Version (https://www.python.org/ftp/python/3.8.9/python-3.8.9-amd64.exe)
    - Visual Studio Community edition 2022 & Desktop development with C++ Workload (https://visualstudio.microsoft.com/thank-you-downloading-visual-studio/?sku=Community&channel=Release&version=VS2022&source=VSLandingPage&passive=false&cid=2030)
    
## Installations: 

    - pip install cmake 
    - pip install dlib
    - pip install face-recognition 
    - pip install opencv-python-headless
    - pip install opencv-contrib-python
    - pip install opencv-python 
    - pip install easyocr 
    - pip install matplotlib
    - pip install messagebox
    
 ## Running System:
 
    - Execute program by running main.py

The recent Omicron outbreak in New Zealand has brought forward an array of socio-economic complications. It has had a significant impact on our domestic economy, especially the small businesses which are suffering the most. From not being able to operate their businesses over the lockdown period. 

Our most effective and efficient way of dealing with our current outbreak is to have as much of the population double vaccinated. As it has been proven to reduce the chances of getting the virus, spreading the virus, and significantly reducing the health implications of the virus.

As we start to reach target percentages set by the local District Health Boards, it will be vital that businesses and educational institutions comply with government regulations, and enforce entry to the vaccinated only. 

However, with the current approach of verifying vaccination certificates, there are a number of significant flaws. Firstly, the system is easy to cheat against, a non-vaccinated individual is able to use someone else's certificate, acting as if it was theirs. The only option here is to have the businesses check the Vaccination certificates and then cross verifying with a form of government-approved Photo Identification. This is a time-consuming task to conduct, and it requires businesses to dedicate an employee to this task.

At a time when businesses are recovering from financial losses, this brings an additional overhead. It can be noted that businesses are not putting in as much effort in the verification process. Some businesses are not cross-verifying the QR codes with a form of identity. This is already demonstrating the fact that the current approach isn't working as well as it was anticipated. 

This project presents a revolutionary method of conducting the vaccination verification process. It utilizes the utmost cutting-edge A.I. technologies to create a highly robust, efficient, effective system. 

The system first verifies the Vaccination details of the user.  The system prompts the user to first submit their My Covid Pass, it then uses Deep Neural Network-based Optical Character Recognition (OCR) to cross verify the Name, and Date of Birth across both the user's driver's license and their My Covid Pass. This way the system is able to effectively abstract the user's vaccination status. (It should be noted that work is currently being undertaken to decode the contents of the encrypted QR code present on the Vaccination pass) 

Following this, the system conducts a verification of the identity of the user, via a form of government-approved photo identification, this may be their driver's license or their passport. The system trains itself on this photo id using the Deep Face algorithm.  This system then links the user's vaccination details to their photo ID. 

Finally, when the system is run, it can correctly verify that the user is vaccinated. Businesses can use the system to completely streamline their verification process. All they need to do is step up the system (Camera, Arduino with the system embedded) on their business premise and run the system, it will automatically start to verify. 

This system is not intended to completely replace what there is currently, instead it provides an alternative that businesses can optionally choose to implement within their services. 

In the future, this system may abstract vaccination details from the My Covid Record database and then train itself to recognize and verify the individual using the photo identification submitted by the Real Me account verification process. 
