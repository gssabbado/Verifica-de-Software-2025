## Session Tests
1. Create session OK
2. Session has unique ID OK
3. Calculate end time OK
4. Check if seat is available OK
5. Get all available seats OK
6. Detect session overlap same room OK
7. No overlap different rooms OK
8. No overlap sequential sessions OK 

## User Tests
1. Create user OK
2. User has unique ID OK
3. User bookings start empty OK

## Booking Tests
1. Create booking
2. Booking has unique ID
3. Booking records current time
4. Calculate total price
5. Booking added to user bookings
6. Booking added to session bookings
7. Confirm booking
8. Confirm fails if any seat not reserved
9. Cancel booking

## Test associations
1. Create room, add session and book seats
2. Prevent double booking
3. Prevent overlapping sessions
4. Session capacity management