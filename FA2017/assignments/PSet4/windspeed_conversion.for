      PROGRAM windspeed_conversion
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c A wind speed conversion program.
c
c By: Kevin Goebbert
c Date: 15 September 2017
c
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      real in_wspd, out_wspd
      character*3 in_wspd_unit, out_wspd_unit
      real mph_to_kts, kts_to_mph, kph_to_mph, mps_to_kph
      real mph_to_mps, kts_to_mps, kph_to_mps, mps_to_kts
      real mph_to_kph, kts_to_kph, kph_to_kts, mps_to_mph

      PRINT *, "*****************************************"
      PRINT *, "* Welcome to Wind Speed Conversion 2000 *"
      PRINT *, "*                                       *"
      PRINT *, "*  Available Wind Speed Units:          *"
      PRINT *, "*    mph = miles per hour               *"
      PRINT *, "*    kts = knots                        *"
      PRINT *, "*    mps = meters per second            *"
      PRINT *, "*    kph = kilometers per hour          *"
      PRINT *, "*                                       *"
      PRINT *, "*****************************************"

      
      PRINT *, "Type in a wind speed with units (e.g., 25 mph):"
      READ(*,*) in_wspd, in_wspd_unit

      PRINT *, "Type desired units:"
      READ(*,*) out_wspd_unit

      print *, ""


      mph_to_kts = 0.868976
      kts_to_mph = (1.0/mph_to_kts)

      mps_to_kts = 1.943844
      kts_to_mps = (1.0/mps_to_kts)

      mps_to_mph = 2.236936
      mph_to_mps = (1.0/mps_to_mph)

      mps_to_kph = 3.6
      kph_to_mps = (1.0/mps_to_kph)

      mph_to_kph = 1.60934
      kph_to_mph = (1.0/mph_to_kph)

      kts_to_kph = kts_to_mps*mps_to_kph
      kph_to_kts = kph_to_mps*mps_to_kts

 101  format(A,f5.1,A4)
      PRINT 101, "Input Wind Speed: ",in_wspd,in_wspd_unit
      print *, ""

      if (out_wspd_unit .eq. in_wspd_unit) then
         out_wspd = in_wspd
         PRINT *, "Warning: No conversion needed due to no change in units"
      else if (out_wspd_unit .ne. in_wspd_unit) then
         if ((out_wspd_unit .eq. 'mph') .and. (in_wspd_unit .eq. 'kts')) then
            out_wspd = kts_to_mph*in_wspd
         else if ((out_wspd_unit .eq. 'mph') .and. (in_wspd_unit .eq. 'kph')) then
            out_wspd = kph_to_mph*in_wspd
         else if ((out_wspd_unit .eq. 'mph') .and. (in_wspd_unit .eq. 'mps')) then
            out_wspd = mps_to_mph*in_wspd
         else if ((out_wspd_unit .eq. 'mps') .and. (in_wspd_unit .eq. 'kph')) then
            out_wspd = kph_to_mps*in_wspd
         else if ((out_wspd_unit .eq. 'mps') .and. (in_wspd_unit .eq. 'kts')) then
            out_wspd = kts_to_mps*in_wspd
         else if ((out_wspd_unit .eq. 'mps') .and. (in_wspd_unit .eq. 'mph')) then
            out_wspd = mph_to_mps*in_wspd
         else if ((out_wspd_unit .eq. 'kts') .and. (in_wspd_unit .eq. 'kph')) then
            out_wspd = kph_to_kts*in_wspd
         else if ((out_wspd_unit .eq. 'kts') .and. (in_wspd_unit .eq. 'mph')) then
            out_wspd = mph_to_kts*in_wspd
         else if ((out_wspd_unit .eq. 'kts') .and. (in_wspd_unit .eq. 'mps')) then
            out_wspd = mps_to_kts*in_wspd
         else if ((out_wspd_unit .eq. 'kph') .and. (in_wspd_unit .eq. 'mps')) then
            out_wspd = mps_to_kph*in_wspd
         else if ((out_wspd_unit .eq. 'kph') .and. (in_wspd_unit .eq. 'mph')) then
            out_wspd = mph_to_kph*in_wspd
         else if ((out_wspd_unit .eq. 'kph') .and. (in_wspd_unit .eq. 'kts')) then
            out_wspd = kts_to_kph*in_wspd
         end if
      end if
      PRINT 101, "Output Wind Speed: ",out_wspd,out_wspd_unit

      end
