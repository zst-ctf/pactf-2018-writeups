I feel confident enough about my encoding that I'll tell you exactly how I did it! The public keys
folder has keys numbered 0 through 19. I simply encoded the bytes of a message (in big-endian
order), applied key 0, key 1, and so on until key 19. The message is basic ASCII: I'll tell you that
much.
