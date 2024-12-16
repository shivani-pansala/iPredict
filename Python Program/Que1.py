'''Write a program which will find all such numbers which are divisible by 7 but are not a
multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a comma-separated sequence on a single line.'''


for i in range(2000, 3201):
    
    if i % 7 == 0 and i * 5 != 0:
          print(i, end=', ')             
            
# Output

2002, 2009, 2016, 2023, 2030, 2037, 2044, 2051, 2058, 2065, 2072, 2079, 2086, 2093, 2100, 2107, 2114, 2121, 2128, 2135, 2142, 2149, 2156, 2163, 2170, 2177, 2184, 2191, 2198, 2205, 2212, 2219, 2226, 2233, 2240, 2247, 2254, 2261, 2268, 2275, 2282, 2289, 2296, 2303, 2310, 2317, 2324, 2331, 2338, 2345, 2352, 2359, 2366, 2373, 2380, 2387, 2394, 2401, 2408, 2415, 2422, 2429, 2436, 2443, 2450, 2457, 2464, 2471, 2478, 2485, 2492, 2499, 2506, 2513, 2520, 2527, 2534, 2541, 2548, 2555, 2562, 2569, 2576, 2583, 2590, 2597, 2604, 2611, 2618, 2625, 2632, 2639, 2646, 2653, 2660, 2667, 2674, 2681, 2688, 2695, 2702, 2709, 2716, 2723, 2730, 2737, 2744, 2751, 2758, 2765, 2772, 2779, 2786, 2793, 2800, 2807, 2814, 2821, 2828, 2835, 2842, 2849, 2856, 2863, 2870, 2877, 2884, 2891, 2898, 2905, 2912, 2919, 2926, 2933, 2940, 2947, 2954, 2961, 2968, 2975, 2982, 2989, 2996, 3003, 3010, 3017, 3024, 3031, 3038, 3045, 3052, 3059, 3066, 3073, 3080, 3087, 3094, 3101, 3108, 3115, 3122, 3129, 3136, 3143, 3150, 3157, 3164, 3171, 3178, 3185, 3192, 3199,
