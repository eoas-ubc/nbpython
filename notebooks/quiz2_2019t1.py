# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_filter: all
#     notebook_metadata_filter: all,-language_info
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   latex_envs:
#     LaTeX_envs_menu_present: true
#     autoclose: false
#     autocomplete: true
#     bibliofile: biblio.bib
#     cite_by: apalike
#     current_citInitial: 1
#     eqLabelWithNumbers: true
#     eqNumInitial: 1
#     hotkeys:
#       equation: meta-9
#     labels_anchors: false
#     latex_user_defs: false
#     report_style_numbering: false
#     user_envs_cfg: false
#   latex_metadata:
#     chead: Quiz 2, October 17, 2019 -- SOLUTIONS
#     lhead: EOSC 340
#   toc:
#     base_numbering: 1
#     nav_menu: {}
#     number_sections: false
#     sideBar: false
#     skip_h1_title: false
#     title_cell: Table of Contents
#     title_sidebar: Contents
#     toc_cell: false
#     toc_position: {}
#     toc_section_display: false
#     toc_window_display: false
# ---

# %% [raw] {"ctype": "question", "quesnum": -1}
# \pagestyle{headers}

# %% [markdown] {"trusted": true, "ctype": "question", "quesnum": -1}
# Name (Last, First):
# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
#
# Student Number:
# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
#
# Signature:
# \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_
#
# **This is exam packet (A)**
#
# **Verify that (A) in the ``Test Form'' column of your bubble sheet has been marked**
#
# **Instructions:** You may detach the Bubble sheet (first page) and the
# Equation Sheet (last page) from this exam package. No notes, books,
# cellphones or aids are allowed. Calculators are okay.
# Only answers indicated on the provided Bubble sheet will be marked.
# You must submit both this ``question book'' as well as the Bubble sheet
# before leaving the room.
#
# **Course Statistics** Find the `HOURS STUDIED` area on your Bubble sheet. In the past week, how much time did you spend studying for this exam? Please enter your answer in the `HOURS STUDIED` area of your Bubble sheet. Round to the nearest hour. If, for example, you spent 2 hours studying, enter `002`. If, for example, you spent 14 hours studying, enter `014`.
#
# **This exam booklet should contain 9 questions.**
#
# %% [raw] {"ctype": "question", "quesnum": -1}
#
# \newpage

# %% [markdown] {"ctype": "question", "quesnum": 1}
# Q1) We notice the planet loses about $5 \times 10^{5}\ km^{2}$ of ice
#     area for each 1 K change in surface temperature. Further, the
#     change in radiative forcing per square kilometre of arctic ice
#     ∆R/∆(ice area) is $-10^{−6} W m^{- 2}/km^{2}$. Use this
#     information to calculate the strength of the ice-albedo feedback
#     $f_{ice}$. Choose the closest answer.
#
#    A) 0.2 $\text{Wm}^{- 2}K^{- 1}$
#
#    B) 0.5 $\text{Wm}^{- 2}K^{- 1}$
#
#    C) 0.75 $\text{Wm}^{- 2}K^{- 1}$
#
#    D) 2 $\text{Wm}^{- 2}K^{- 1}$
#
#    E) 5 $\text{Wm}^{- 2}K^{- 1}$
#
# %% [markdown] {"ctype": "answer", "quesnum": 1}
# **Q1 answer B)**
#
# \begin{align*}
# f_{ice} & =  \left( \frac { \Delta R } { \Delta \text {ice area } } \right) \left( \frac { \Delta \text { ice area} } { \Delta T } \right) \\
# & = \left ( -5 \times 10^{-5} \right ) \left ( -10^{-6} \right ) = 0.5
# \end{align*}

# %% {"ctype": "answer", "quesnum": 1}
# try it in python

fice = -5.e5*(-1.e-6)  #B
print(f"B) ice feedback is {fice} W/m^2/K")

# %% [markdown] {"ctype": "question", "quesnum": 2}
# Q2) Suppose a climate scientist establishes that her group’s model
#     has a total climate sensitivity of λ=0.65 K/($Wm^{-2}$). She then
#     makes a change to the cloud routine that increases the strength of
#     the cloud feedback from +0.5 $\text{Wm}^{- 2}K^{- 1}$ to +0.75
#     $\text{Wm}^{- 2}K^{- 1}$. What is the new total feedback of the
#     model?
#
#    A) 0.90 $\text{Wm}^{- 2}K^{- 1}$
#
#    B) -0.90 $\text{Wm}^{- 2}K^{- 1}$
#
#    C) 1.29 $\text{Wm}^{- 2}K^{- 1}$
#
#    D) -1.29 $\text{Wm}^{- 2}K^{- 1}$
#
#    E) 1.79 $\text{Wm}^{- 2}K^{- 1}$
# %% [markdown] {"ctype": "answer", "quesnum": 2}
# **Q2 Answer: D)**
#
# Approach -- first find the total feedback by inverting the sensitivity, then add the extra cloud feedback and change back to find the new sensitivity
#
#

# %% {"ctype": "answer", "quesnum": 2}
# try it in python

f = -1/0.65
#
# increase the cloud feedback
#
f_new = f + 0.25
lambda_new = -1/f_new
print(f"new feedback is {f_new} W/m^2/K, new sensitivity is {lambda_new} K/(W/m^2)")

# %% [markdown] {"ctype": "question", "quesnum": 3}
# Q3) How long does it take for a constant forcing of 3 $W\,m^{- 2}$ to
#     warm a 150 m thick ocean layer by 0.75 K? (A year has 31,536,000
#     seconds)
#
#    A) 5 years
#
#    B) 7.5 years
#
#    C) 10 years
#
#    D) 15 years
#
#    E) 25 years
# %% [markdown] {"ctype": "answer", "quesnum": 3}
# **Q3 answer A)**

# %% {"ctype": "answer", "quesnum": 3}
#Try it in python

D=150   #m
cw=4186  #J/kg/K
rhow=1000.  #kg/m%3
delTemp =0.75  #K
delF = 3  #W/m^2
delt = rhow*D*cw*delTemp/delF  #seconds
sec2years=1/(31536000)  #years
print(f"time is {delt*sec2years} years")  #A

# %% [markdown] {"ctype": "question", "quesnum": 4}
# Q4) Imagine we end up burning the rest of the available coal (2800 Gton
#     carbon) **and** the oil and natural gas (200 Gton carbon), but we
#     don’t burn any other fossil carbon. What will the atmospheric
#     concentration of $CO_2$ be when we’re finished? Assume we
#     burn everything instantaneously, that all of the emitted carbon
#     stays in the atmosphere, and that today’s atmospheric $CO_2$
#     concentration is 400 ppm.
#
#    A) about 580 ppm  
#    B) about 640 ppm  
#    C) about 1050 ppm  
#    D) about 1200 ppm  
#    E) about 1830 ppm
# %% [markdown]
# **Q4) E**

# %% {"ctype": "answer", "quesnum": 4}
#python
before = 400 #pp
increase=3000/2.1
new_concentration = before + increase
print(f"new concentration {new_concentration}")
# %% [raw] {"ctype": "question", "quesnum": 4}
# \newpage
# %% [markdown] {"ctype": "question", "quesnum": 5}
# Q5) For the figure below, pick the most accurate description of the
#     rectangular region labeled (2).  Assume the instrument is looking down from the top of this atmosphere
#
#    <!-- <img src="quiz2_media/image14.png" style="width:4.96063in;height:4in" /> -->
#    ![Figure 1](quiz2_media/image14.png)
#
#    A) The radiation emitted by the gas that reaches the top of the atmosphere  
#    B) The radiation absorbed by the gas  
#    C) The greenhouse effect from the gas in this wavenumber range  
#    D) The surface radiation absorbed by the gas  
#    E) The radiation emitted by the gas that reaches the surface
#
# %% [markdown] {"ctype": "answer", "quesnum": 5}
# **Q5) answer C) -- top - bottom is the greenhouse effect**

# %% [raw] {"ctype": "question", "quesnum": -1}
# \newpage
# %% [markdown] {"ctype": "question", "quesnum": 6}
# Q6) For this feedback loop:
#
# <!-- <img src="quiz2_media/image16.png" style="width:4.62205in;height:1.50394in" /> -->
#  
# ![Figure 2](quiz2_media/image16.png)
#
#   Choose the best characterization, keeping in mind that feedbacks
#   work in both directions.  ($R_{net}$ is the net downward radiation at the top of the atmosphere)
#
#    A) Amplifying because increasing low clouds heat the surface through
#       longwave emission  
#    B) Stabilizing because increasing low clouds reduce the surface heat
#       flux  
#    C) Amplifying because increasing low clouds reflect more incoming
#       shortwave  
#    D) Amplifying because increasing low clouds increase atmospheric
#       mixing  
#    E) Stabilizing because increasing low clouds emit more radiation to
#       space
# %% [markdown] {"ctype": "answer", "quesnum": 6}
# **Q6) Answer is C) -- if low clouds cool, then reducing them will heat, so amplifying**

# %% [raw] {"ctype": "question", "quesnum": -1}
# \newpage
#
# %% [markdown] {"ctype": "question", "quesnum": 7}
# Q7) Consider the following shallow, nocturnal atmospheric layer with
#     emissivity **$ε_a$=0.8** over ground with emissivity of ε=1. If
#     the ground temperature $T_g$ is 300 K and the air
#     temperature $T_a$ is 260 K, what is the heating/cooling rate
#     **of the ground** in $W\,m^{-2}$?
#
#    **(Note 250 $W\,m^{-2}$ in longwave flux is entering the layer from above)**
#
#    **Shortcut:  $\sigma \times 300^4 = 460\ W\,m\,^2$**
#
#       
#    <!-- <img src="quiz2_media/image17.png" style="width:4.89764in;height:2.23228in" /> -->
#    ![Figure 3](quiz2_media_resize/image17.png)
#
#       
#    A) -251 $W\,m^{-2}$  
#    B) -202 $W\,m^{-2}$  
#    C) +101 $W\,m^{-2}$  
#    D) +202 $W\,m^{-2}$  
#    E) +251 $W\,m^{-2}$

# %% [markdown] {"ctype": "answer", "quesnum": 7}
# **Q7) Answer is B -- ground is cooling**

# %% {"ctype": "answer", "quesnum": 7}
# do it in python

sigma=5.67e-8
Ta = 260 #K
flux_ground = 460 #W/m^2
eps = 0.8
flux_top = 250.  #W/m^2
heating_rate = flux_top*(1 - eps) + eps*sigma*Ta**4. - flux_ground  
print(f"heating rate for surface {heating_rate} W/m^2")

# %% [markdown] {"ctype": "question", "quesnum": 8}
# Q8) Which of the following climate feedbacks are always stabilizing?  
#       
#     i. Water vapour feedback  
#     ii. Lapse rate feedback  
#     iii. Planck feedback  
#     iv. cloud feedback  
#       
#    A) i, iii  
#    B) ii,iii  
#    C) iv  
#    D) i, iii, iv  
#    E) ii, iv
# %% [markdown] {"ctype": "answer", "quesnum": 8}
# **Q8 answer is B) -- lapse rate feed back and planck feedback**

# %% [raw] {"ctype": "question", "quesnum": -1}
# \newpage
#
# %% [markdown] {"ctype": "question", "quesnum": 9}
# Q9) Given the fluxes in the following figure, the Greenhouse effect of
#     this atmosphere is
#
#    <!-- <img src="final_2018t2/media/image18.png" style="width:3.54331in;height:1.56299in" /> -->
#    ![Figure 4](quiz2_media/single_layer.png)
#
#    A) 20 $W\,m^{-2}$  
#    B) 40 $W\,m^{-2}$  
#    C) 120 $W\,m^{-2}$  
#    D) 320 $W\,m^{-2}$  
#    E) 400 $W\,m^{-2}$
#
#
# %% [markdown] {"ctype": "answer", "quesnum": 9}
# **Q9) Correct answer is B)**

# %% {"ctype": "answer", "quesnum": 9}
# python for Q9
#
#  at the top level

Ia = -280.  #W/m^2
Ig = -400.  #W/m^2
Ig_top = -80.
greenhouse = (Ia + Ig_top) - Ig
print(f"the greenhouse effect is {greenhouse} W/m^2")
# %% [raw] {"ctype": "question", "quesnum": " "}
# \newpage
#
# %% [markdown]
# \begin{align}
# \text{Layer energy equation:} ~~~ & \frac { d E } { d t } = I _ { \downarrow } + I _ { \uparrow }\\
# \text{Solar constant:}~~~& S= \frac { S _ { 0 } } { 4 } ( 1 - \alpha )\\
# \text{Total grey body flux} ~~~ & I = \varepsilon \sigma T ^ { 4 }\\
# &\text{where} ~~~ \sigma = 5.67 \times 10 ^ { - 8 } \mathrm { Wm } ^ { - 2 } \mathrm { K } ^ { - 4 }\nonumber\\
# \text{transmissivity tr:}~~~& I _ { \text {transmitted } } = \mathrm { tr } I _ { 0 }\\
# \text{reflectity}~ \alpha~~~ & I _ { \text {reflected } } = \alpha I _ { 0 } \\
# \text{absorbtivity abs} ~~~ & I _ { \text {absorbed} } = \text{abs} I _ { 0 }\\
# \text{Kirchoff's law} ~~ & \varepsilon = \text{abs} \\
# \text{$CO_2$ radiative forcing} ~~~& \Delta F = \left(3.8 \mathrm{W} \mathrm{m}^{ - 2 } \right) \frac { \ln ( \text {newp} \operatorname { CO } 2 / \text { origp } \mathrm { CO } 2 ) } { \ln ( 2 ) } \\
# \text{Conservation of Energy:}~~~&\alpha \mathrm { I } _ { 0 } + a b s \mathrm { I } _ { 0 } + \mathrm { trI } _ { 0 } = \mathrm { I } _ { 0 }\\
# \text{moist static energy:}~~~ & h _ { m } = c _ { p } T + l _ { v } w _ { v } + g z \\
# \text{moist adiabatic lapse rate:}~~~&\Gamma = \frac { d T } { d z } = \frac { - g } { c _ { p } + l _ { v } \frac { d w _ { v } } { d T } }\\
# \text{hydrostatic balance:}~~~&d p = - \rho g d z \\
# \text{mass in a layer in $kg/m^2$:}~~~&M = \int _ { z _ { 1 } } ^ { z _ { 2 } } \rho(z) d z\\
# \text{energy in an ocean layer:}~~~&\Delta E=\rho_{w} D c_{w} \Delta T\\
# \text{Conservation of energy for layer:}~~~&\frac{d \Delta E}{d t}=\Delta F\\
# \text{change of temperature for an ocean layer:}~~~&\frac{d \Delta T}{d t}=\frac{\Delta F}{\rho_{w} c_{w} D}\\
# \text{Planck feedback:}~~~&\frac { d I _ { G } } { d T } = \frac { d \left( - \sigma T ^ { 4 } \right) } { d T } = f_{planck} =- 4 \sigma T ^ { 3 } = - 1 / \lambda\\
# \text{Conservation of energy with feedback:}~~~&
# \frac { \Delta E } { d t } = \Delta F - 4 \sigma T ^ { 3 } \Delta T\\
# \text{Climate adjustment to abrupt forcing:}~~~&\Delta T ( t ) = \lambda \Delta F \left( 1 - e ^ { - t / \tau } \right) \\
# \text{Climate adjustment timescale:}~~~&\tau = \rho _ { w } c _ { w } D \lambda\\
# \text{Climate sensitivity:}~~~&\Delta T = \lambda \Delta F\\
# \text{Climage mean temperature budget:}~~~&\rho _ { w } c _ { w } D \frac { d T } { d t } = \Delta F + \sum f _ { n } \Delta T\\
# \text{Climate feedback factor:}~~~&f _ { n } = \frac { \Delta R } { \Delta T } = \left( \frac { \Delta R } { \Delta \text { climate } } \right) \left( \frac { \Delta \text { climate } } { \Delta T } \right)\\
# \text{Climate sensitivity with feedbacks:}~~~&\lambda = - \frac { 1 } { \sum f _ { n } }
# \end{align}

# %% [markdown]
# # Quiz 2 constants
#
# \begin{align}
# &\text{1 ppm = 2.1 Gtonnes Carbon = 7.6 Gtonnes $CO_2$}\\
# \sigma  &= 5.67 \times 10 ^ { - 8 } \mathrm { Wm } ^ { - 2 } \mathrm { K } ^ { - 4 }\\
# c_p  &= 1004\ J\,kg^{-1}\,K^{-1} \\
# c_w  &= 4186\ J\,kg^{-1}\,K^{-1} \\
# \rho_w &= 1000\ kg\,m^{-3}\\
# l_v &= 2.5 \times 10^6\ J\,kg^{-1}
# \end{align}
