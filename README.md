# Samsung Smart TV API for Q-SYS

Control Samsung TVs exposing the local Tizen v2 WebSocket remote interface, including Frame Art Mode On, Off and reported status. This is the external network interface; it does not run Samsung's TV-side Product API. No SmartThings account, API key, external server or TV-side app is required.

Plugin and package version: **1.0.0.3**.

## Install with Q-SYS Library

1. Sign in to [Q-SYS Library](https://library.qsys.com/my-library).
2. Open **My Packages → Add Personal Package**.
3. Enter **Samsung Smart TV API** and this package URL:

   ```text
   https://joshua-small.github.io/qsys-samsung-smart-tv/registration/joshuasmall.qsys.samsungsmarttv/index.json
   ```

4. In Designer, sign in with the same QSC ID and open **Tools → Show Asset Installer**.
5. Refresh **Available Assets**, select the package and install it.

For manual installation, download `SamsungSmartTV.qplug` from [Releases](https://github.com/joshua-small/qsys-samsung-smart-tv/releases) and place only that file in your Documents folder under `QSC/Q-Sys Designer/Plugins`. Keep backups and support files outside Plugins. Use one installation method to avoid duplicate copies. Refreshing/installing a package does not deploy changes to a Core; update and test the design before **Save to Core & Run**.

## Connect and pair

1. Add **Samsung > Smart TV** to a test design. Start with **Transport = TLS (8002)**. Enable **Frame Art Mode** only for a compatible TV.
2. Run the design, enter the TV address on Setup and press **Connect / Pair**. Keep the TV on and approve the prompt with its remote. Enable network power-on/IP remote access where the TV provides those settings.
3. **Remote authorized** confirms the remote session. The Frame page reports Art availability separately. Test Read Art Mode, On and Off against the screen.
4. For Wake-on-LAN, enter the TV MAC address and appropriate broadcast address. Power On sends a UDP magic packet to port 9; wake support depends on TV settings and the network.

| Page | Functions |
| --- | --- |
| Setup | Address, pairing, disconnect, forget token, wake settings and connection status |
| Controls | Power, volume steps, mute toggle, source/HDMI keys and app-ID launch |
| Remote | Navigation, digits, playback, color keys and a custom KEY_* command |
| Frame | Art On/Off, read status and feedback validity |

HDMI sends KEY_HDMI, not a guaranteed discrete input selection. Volume/mute use step/toggle commands. The interface does not provide reliable absolute volume or power/input/mute readback. Read ArtState only while ArtValid is true. Art Off leaves Art Mode; it does not request power-off. Commands queued before disconnection are discarded.

## Pairing and compatibility

Targets Q-SYS Designer/Core 10.5. Model/year and firmware support vary. Source/protocol tests passed, but native Designer rendering, token persistence, Core networking and physical-TV acceptance remain open.

Pairing tokens are acquired at runtime and stored in the design, never bundled in this plugin or printed by its debug logging. Treat paired designs as containing credentials. Forget Token clears local storage; remove the controller in the TV device list to revoke TV-side access. WSS uses port 8002 with no automatic downgrade. Plain port 8001 must be selected explicitly.

Protocol reference: [samsung-tv-ws-api](https://github.com/xchwarze/samsung-tv-ws-api/tree/e48d6377faede37db1f034d726a079b9d8034fac). This Lua plugin does not bundle that Python library. MDC, ExLink, SmartThings cloud, app discovery and artwork upload are outside this plugin.

## Support

Report bugs through [Issues](https://github.com/joshua-small/qsys-samsung-smart-tv/issues), including plugin version, Q-SYS version, device/broker model and firmware, and reproduction steps. Remove credentials from logs and design files before sharing them.

This is an independent personal package, not a Q-SYS Verified Asset or a manufacturer-endorsed release. Manufacturer names and logos identify compatible products. Existing source attribution is retained.

### Offline package checks

Run `python3 scripts/verify.py` and `python3 -m unittest discover -s tests -p test_package_identity.py`. Before a release, run `python3 scripts/verify.py --release-tag v<VERSION>`. The exact tag, project package version and `PluginInfo.Version` must agree. `BuildVersion` is a separate optional SDK field. These checks do not establish Designer or hardware acceptance.
