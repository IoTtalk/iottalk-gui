class _Set extends Set {
  issubset(s) {
    for(const el of this) {
      if (!s.has(el))
        return false;
    }
    return true;
  }
}


export default {
  Set: _Set,
}
