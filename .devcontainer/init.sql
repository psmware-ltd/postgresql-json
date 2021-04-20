--  SPDX-License-Identifier: AGPL-3.0-only

--  Geras is a time recording application written specifically for
--  the Alzheimer Society of Ireland
--  Copyright (C) 2020-2021  Patrick McLean - psmware ltd

--  This program is free software: you can redistribute it and/or modify
--  it under the terms of the GNU Affero General Public License as published by
--  the Free Software Foundation, either version 3 of the License, or
--  (at your option) any later version.

--  This program is distributed in the hope that it will be useful,
--  but WITHOUT ANY WARRANTY; without even the implied warranty of
--  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
--  GNU Affero General Public License for more details.


DO
$do$
BEGIN
    IF NOT EXISTS (
        SELECT FROM pg_catalog.pg_roles  -- SELECT list can be empty for this
         WHERE  pg_roles.rolname = 'jsondb') THEN

        CREATE USER jsondb WITH ENCRYPTED PASSWORD 'supersecretpassword';
        ALTER USER jsondb CREATEDB;
    END IF;
END
$do$;

