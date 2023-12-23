# loggerjava

---
an easy logger which outputs like java
### how to use

use the following codes:

import loggerjava

logger = loggerjava

logger.info("test")

logger.warn("test",pos="insidecommand")

### output
[20:39:00] [main/debug]: test

[20:39:00] [main/info]: test

[20:39:00] [main/WARNING]: test

[20:39:00] [main/ERROR]: test

[20:39:00] [main/FATAL]: test

### config

logger.confg()

### versions

0.0.4 upgrade the config sys and add helps

0.0.3 upload the descriptions

0.0.2 initial upload