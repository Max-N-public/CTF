
bar2()
{
  buf [38];

  
local_10 = input
  traverse = 0;
  while (traverse < 36)
{
  index = 0;
  while (index < 0x24)
  {
    if ((int)auStack168[index] < 100)
    {
      if (((int)auStack168[index] < 0x5b) && (0x1f <   (int)auStack168[index]))
      {
        auStack168[index] = auStack168[index] + 0x23;
      }
      else
      {
        auStack168[index] = auStack168[index] + 0x20;
      }
    }
    else
    {
      auStack168[index] =
           auStack168[index] + ((lParm1 + index + 1);
      auStack168[index] =
           (int)(auStack168[index] + (auStack168[index] >> 0x1f)) >> 1;
    }
    index = index + 1;
  }





  local_ac = 0;
  do {
    if (0x23 < local_ac) {
      uVar1 = 1;
LAB_00100b39:
      if (local_10 != *(long *)(in_FS_OFFSET + 0x28)) {
                    /* WARNING: Subroutine does not return */
        __stack_chk_fail();
      }
      return uVar1;
    }
    if (auStack168[local_ac] != *(uint *)(lParm2 + local_ac * 4)) {
      uVar1 = 0;
      goto LAB_00100b39;
    }
    local_ac = local_ac + 1;
  } while( true );
}

