# 1/24/23 Made By Jibril 
# https://en.wikipedia.org/wiki/Intercontinental_ballistic_missile#:~:text=Flight%20phases,-The%20following%20flight&text=reentry%2Fterminal%20phase%20(starting%20at,see%20also%20maneuverable%20reentry%20vehicle. 

# General Info 
# V = Velocity
# Δ = Change in X 
# S = Start Of A Phase 
# E = End Of A Phase

# Projectile Info 
# Name = X 
# Total Moves = X
# Explotion Radis = X 
# totalMoves = 5

# Function 
# 
# 
#
# Notes 
# You will Start with Three and are not Renewable 
#
# It Will Dednate at Y30Km, Rather than Y0Km. Because a
# of a AirBurst  
#
# I might add a alt deadnation in the future where it denaates 
# at Y0Km to add variton in use

# Info 
# Velocity Range = 0Kmh -> 24000.0Kmh -> 0Mph -> 15000.0Mph
# X-Axis Range   = 0km  -> 7822.0Km   -> 0Mi  -> 4860.0Mi
# Y-Axis Range   = 0km  -> 4500.0Km   -> 0Mi  -> 2796.1Mi 

# Boost Phase = 2 Moves  
# Boost Phase  ΔY-Axis   = S0km - E1200Km     -> S0Mi - E750Mi   
# Boost Phase  ΔX-Axis   = S0km - E3905       -> S0mi - E2426Mi
# Boost Phase  ΔVelocity = S0Kmh - E14000Kmh ->  S0Mi  -E14914Mph
#   
# Mid Course = 1 Move      
# Mid Course ΔY-Axis       = S1200Km - E4500Km -> S750Mi   - E2796Mi 
# Mid Course ΔX-Axis       = S2000Km - E5569km -> S1242Mi  - E2426Mi 
# Mid Course ΔVelocity     = S14000Kmh - E24000Kmh -> S8700Mph - E14914.24Mph 
# b dbn
# ReEntry Phase = 2 Moves  
# ReEntry Phase  ΔY-Axis   = S4500km - E0Km     -> S2796Mi - E500    
# ReEntry Phase  ΔX-Axis   = S5569km - E7822Km  -> S2426Mi - E14914.24 
# ReEntry Phase  ΔVelocity = S24000Kmh - 100Kmh -> S14914.24Mph - 62Mph


# Start Of Expected OutPut

# Phase = N/A
# Name = Nuke[X] 
# Move = 0 
# Pos = S(0,0) -> E(0,0)
# Velocity = 0Kmh
# ETA = 5 Moves

# Phase = Boost Phase 
# Name = Nuke[X] 
# Move = 1 
# Pos = S(0,0) -> E(1150,2000)
# Velocity = 7000Kmh
# ETA = 4 Moves

# Phase = Boost Phase 
# Name = Nuke[X] 
# Move = 2
# Pos = S(1150,2000) -> E(2750,4000)
# Velocity = 14000Kmh
# ETA = 3 Moves

# Phase = Mid Course 
# Name = Nuke[X] 
# Move = 3
# Pos = S(2750,4000) -> E(5150,4000)
# Velocity = 24000Kmh
# ETA = 2 Moves

# Phase = ReEntry Phase 
# Name = Nuke[X] 
# Move = 4
# Pos (5150,4000) -> (7837,30)
# Velocity = 12000Kmh
# ETA = 1 Moves

# Phase = ReEntry Phase 
# Name = Nuke[X] 
# Move = 5
# Pos (7837,30) -> (Boom)
# Velocity = 4000Kmh
# ETA = 0 Moves

# End Of Expected OutPut
