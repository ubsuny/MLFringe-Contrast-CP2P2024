<img width="761" alt="Screenshot 2024-03-27 at 5 20 19 PM" src="https://github.com/ubsuny/MLFringe-Contrast-CP2P2024/assets/13534352/220a95cd-02ba-4373-9e77-4fbdee8cc9c4"># Fringe Contrast/Visibility
## A direction towords the project
Recent advancements in phase-grating moiré interferometry (PGMI) position it as a disruptive technology for the future of neutron interferometry. PGMIs facilitate the exploitation of polychromatic beams and the direct capture of interference patterns using existing neutron camera technology. However, current modeling approaches for diverse PGMI configurations are hindered by computationally expensive numerical calculations and backward propagation techniques. This research presents a paradigm shift by introducing a novel k-space model for PGMI setups illuminated by cone beams. This model leverages a generalized Fresnel scaling theorem, resulting in an intuitive forward propagation approach applicable to a wide parameter space. We demonstrate that PGMI interference embodies a unique manifestation of the Talbot effect, with optimal fringe visibility achieved at the moiré coincidence of Talbot distances. Analytical expressions are derived for contrast and propagating intensity profiles across various scenarios. Furthermore, we investigate the behavior of the dark-field imaging signal, crucial for sample characterization. The model's predictive capabilities are validated through rigorous experimental comparisons, demonstrating exceptional concordance. Finally, we propose and experimentally verify a method to recover contrast at previously inaccessible PGMI autocorrelation lengths. This work establishes a comprehensive toolkit for the analysis and comprehension of existing PGMI setups, paving the way for future advancements such as two-dimensional PGMIs and the characterization of intricate samples.[1]
Generalize the Fresnel scaling theorem to introduce a k-space model for PGMI (phase-grating moire interferometry) setups illuminated by a cone beam, enabling an intuitive forward propagation model for a wide range of parameters 

## Fringing
 The interaction of identical waves from at least two sources produces interference fringes.
 ![fring](https://github.com/ubsuny/MLFringe-Contrast-CP2P2024/assets/13534352/ac2ff89a-4404-4641-b648-8f20a9bb644c) [2]
## Some terminologies
#### Moire interference
is a visual illusion that appears when two similar patterns are overlaid on top of each other.
![moire](https://github.com/ubsuny/MLFringe-Contrast-CP2P2024/assets/13534352/08368897-2258-4ca5-ad12-61a729a9ec67) [3]

#### Talbot effect
It describes how, under certain conditions, a wave can self-image at specific distances after passing through a periodic structure, like a diffraction grating.
### Measuring the intensity.
The intensity equations in the paper [1], are reproduced, the detailes are available in the paper, for now, I have reproduced the intensity profiles for one and two PGMI setups, from the following equations,
<img width="761" alt="Screenshot 2024-03-27 at 5 20 19 PM" src="https://github.com/ubsuny/MLFringe-Contrast-CP2P2024/assets/13534352/79308403-59da-4877-aab8-cfae1d4207db">

<img width="756" alt="Screenshot 2024-03-27 at 5 20 29 PM" src="https://github.com/ubsuny/MLFringe-Contrast-CP2P2024/assets/13534352/de3723fa-06a8-4330-8581-a00f04e64872">
In the equation 12, $ \alpha $ is just taken to be $ \pi/2 $,






**Data types** <br>

As my project will be python base, I will be using, int., char., float, list and string, at least that is what I know so far. I will update it once there is anyhing new. <br>
**Random numbers** <br>
Well, I will be working on measuring the fring visibility/contrast, so I will be dealing with a lot of parameters, say, different diffraction grating, different grating periods, different neutron beams, different distances in the setup, different wavlengths, and so on. I am expecting different uncertinities in those parameters and that is why I would need random numbers in my project. 
I have created an example code, which can calculate the random numbers for different parameters. Please note that this is just an example, and by the time I will need this, I can replace or add the actual parametrs etc. 

## References:
[1] Sarenac, D., Gorbet, G., Kapahi, C., Clark, C. W., Cory, D. G., Ekinci, H., ... & Pushin, D. A. (2023). Cone beam neutron interferometry: from modeling to applications. arXiv preprint arXiv:2309.01787.
[2] https://en.wikiversity.org/wiki/Physics/Fringes
[3] https://www.researchgate.net/figure/Demonstration-of-the-Moire-effect_fig5_308010888
