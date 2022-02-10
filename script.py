print('Welcome.')
encoder_or_decoder = input('Would you like to use the Encoder or Decoder? ')

choose_encoder = True

if encoder_or_decoder == 'encoder':
  choosen_encoder = True

if encoder_or_decoder == 'decoder':
  choosen_encoder = False

if choosen_encoder == True:
  print('Welcome to The Encoder.')
  real_message = input('What is your message? ')
  fake_message = ''
  index = 0
  for word in real_message:
    if word == 'q':
      fake_message += ('a')
    elif word == 'w':
      fake_message += ('b')
    elif word == 'e':
      fake_message+= ('c')
    elif word == 'r':
      fake_message += ('d')
    elif word == 't':
      fake_message+= ('e')
    elif word == 'y':
      fake_message += ('f')
    elif word == 'u':
      fake_message += ('g')
    elif word == 'i':
      fake_message += ('h')
    elif word == 'o':
      fake_message+= ('i')
    elif word == 'p':
      fake_message += ('j')
    elif word == 'a':
      fake_message+= ('k')
    elif word == 's':
      fake_message += ('l')
    elif word == 'd':
      fake_message += ('m')
    elif word == 'f':
      fake_message += ('n')
    elif word == 'g':
      fake_message+= ('o')
    elif word == 'h':
      fake_message += ('p')
    elif word == 'j':
      fake_message+= ('q')
    elif word == 'k':
      fake_message += ('r')
    elif word == 'l':
      fake_message += ('s')
    elif word == 'z':
      fake_message += ('t')
    elif word == 'x':
      fake_message+= ('u')
    elif word == 'c':
      fake_message += ('v')
    elif word == 'v':
      fake_message+= ('w')
    elif word == 'b':
      fake_message += ('z')
    elif word == 'n':
      fake_message += ('y')
    elif word == 'm':
      fake_message += ('z')
    else:
      fake_message += (' ')
    index += 1
  print(fake_message)

if choosen_encoder == False:
  print('Welcome to The Decoder.')
  real_message = input('What is your message? ')
  fake_message = ''
  index = 0
  for word in real_message:
    if word == 'a':
      fake_message += ('q')
    elif word == 'b':
      fake_message += ('w')
    elif word == 'c':
      fake_message+= ('e')
    elif word == 'd':
      fake_message += ('r')
    elif word == 'e':
      fake_message+= ('t')
    elif word == 'f':
      fake_message += ('y')
    elif word == 'g':
      fake_message += ('u')
    elif word == 'h':
      fake_message += ('i')
    elif word == 'i':
      fake_message+= ('o')
    elif word == 'j':
      fake_message += ('p')
    elif word == 'k':
      fake_message+= ('a')
    elif word == 'l':
      fake_message += ('s')
    elif word == 'm':
      fake_message += ('d')
    elif word == 'n':
      fake_message += ('f')
    elif word == 'o':
      fake_message+= ('g')
    elif word == 'p':
      fake_message += ('h')
    elif word == 'q':
      fake_message+= ('j')
    elif word == 'r':
      fake_message += ('k')
    elif word == 's':
      fake_message += ('l')
    elif word == 't':
      fake_message += ('z')
    elif word == 'u':
      fake_message+= ('x')
    elif word == 'v':
      fake_message += ('c')
    elif word == 'w':
      fake_message+= ('v')
    elif word == 'x':
      fake_message += ('b')
    elif word == 'y':
      fake_message += ('n')
    elif word == 'z':
      fake_message += ('m')
    else:
      fake_message += (' ')
    index += 1
  print(fake_message)
